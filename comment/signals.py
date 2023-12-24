from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from comment.models import Comment
from info.models import InfoBlog


# post_delete, pre_delete, pre_save


@receiver(post_save, sender=Comment)
def post_save_comment(sender, instance, created, **kwargs):
    if created:
        print('Comment saved. Calculate new rating')
        recalculate_post_rating(instance_post=instance.info_blog)


@receiver(post_delete, sender=Comment)
def post_delete_comment(sender, instance, **kwargs):
    print('Comment deleted. Calculate new rating')
    recalculate_post_rating(instance_post=instance.info_blog)


def recalculate_post_rating(instance_post: InfoBlog):
    comments = instance_post.comments.all()
    total_rating = sum(comment.rating for comment in comments)
    instance_post.rating = total_rating / len(comments) if comments else 0
    instance_post.save()
