"""测试环境用：把用户最后一次设置的密码明文记录到本地 JSON 文件。

Django 只保存密码哈希，无法从数据库反推出明文，因此只能在
set_password 时额外抄一份，供后台用户列表展示。
"""
import json
import os
import threading

from django.conf import settings

PASSWORD_FILE = os.path.join(settings.BASE_DIR, "plaintext_passwords.json")
_lock = threading.Lock()


def _load():
    try:
        with open(PASSWORD_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save(user_id, password):
    with _lock:
        data = _load()
        data[str(user_id)] = password
        tmp = PASSWORD_FILE + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, PASSWORD_FILE)


def get(user_id):
    return _load().get(str(user_id))
