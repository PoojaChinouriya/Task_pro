from django.db import models
from datetime import timedelta


class Todo_Task(models.Model):
    Status = [('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Cancel', 'Cancel'), ('Pending', 'Pending')]
    task_name = models.CharField(max_length=200)
    task_description = models.TextField()
    task_status = models.CharField(max_length=100, choices=Status, default='Pending')
    task_deadline = models.DateField()
    task_created_date = models.DateField(auto_now_add=True)
    task_completed = models.DateField(auto_now_add=True)

    def save(self, ):
        if not self.pk:
            super(Todo_Task, self).save()
        if self.task_status == 'Completed':
            self.task_completed = self.task_deadline
        else:
            if self.task_created_date and self.task_deadline:
                self.task_completed = self.task_created_date + timedelta(
                    days=(self.task_deadline - self.task_created_date).days)
        super(Todo_Task, self).save()