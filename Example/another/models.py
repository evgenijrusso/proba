from django.db import models
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(_('Name'), max_length=200)

    class Meta:
        verbose_name = _('Task')

    def __str__(self) -> str:
        return f'{self.name}'


class Message(models.Model):
    msg_task = models.ForeignKey(
        'Task', related_name='messages', verbose_name=_('Tasks'),
        on_delete=models.CASCADE, null=True, blank=True)
    msg_text = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = _('Message')

    def __str__(self) -> str:
        return f'{self.text}'
