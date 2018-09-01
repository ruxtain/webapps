from django.db import models
from django.conf import settings

import os
import glob

class Girl(models.Model):
    """
    天梯基础分数 1400 分，和《社交网络》里面一样
    filename 文件的全路径
    rating 对应的分数
    """

    filename = models.CharField(max_length=200)
    rating = models.FloatField(default=1400)

    @property
    def url(self):
        basename = os.path.basename(self.filename)
        return os.path.join('app/images', basename)

    @classmethod
    def sync(cls):
        """ 暂时设计成手动运行，每次有图片更新，运行一次即可
        """
        images = glob.glob('{}/*'.format(settings.IMAGE_PATH))
        for image in images:
            if not cls.objects.filter(filename=image):
                print('Creating {}...'.format(image))
                cls.objects.create(filename=image)

        
