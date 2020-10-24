from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class CalEvent(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True, related_name="schedules")
    title = models.CharField(_('Title'), max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)
    groupId = models.CharField(_('GroupId'), max_length=100, default=False)
    # models.DateTimeField(input_formats=["%d %b %Y %H:%M:%S %Z"])

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

        ordering = ['-start']

    # 관리자 사이트에 표시될 객체 이름 설정
    def __str__(self):
        return self.title
