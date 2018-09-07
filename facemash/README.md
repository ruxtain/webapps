# facemash

使用和电影《社交网络》里面一模一样的评分算法 Elo Rating System，实现一个两两 PK 的评分系统。

![demo image](https://github.com/ruxtain/webapps/blob/master/facemash/demo.jpg)

使用方法：

1. 把图片放入 facemash/app/static/app/images 里面；

2. 配置好数据库（settings.py）；

3. 运行下面的命令：

```
# shell
python manage.py shell

# ipython
In [1]: from app.models import *
In [2]: Girl.sync()

# shell
python manage.py runserver
```