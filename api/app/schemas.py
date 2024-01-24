from marshmallow import Schema


class TaskSchema(Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'deadline')


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
