#DangoDBApp.signals

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TblStudentBasicInfo, TblStudentBasicInfoApplications
from users.models import User, Profile
from users.serializers import TblStudentBasicInfoApplicationsSerializer
from django.contrib.auth.hashers import make_password
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=TblStudentBasicInfo)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print('signals is running')
        try:
            related_application= instance.applicant_id

            user = User.objects.create(
                student_id=instance.student_id,
                name=f"{related_application.first_name} {related_application.middle_name or ''} {related_application.last_name}".strip(),
                email=related_application.email,
                password=make_password(instance.pswrd)  
            )
            print(user)
            Profile.objects.create(user=user)

            logger.info(f"Created new user and profile for student ID: {instance.student_id}")
        except Exception as e:
            logger.error(f"Error creating user and profile for student ID {instance.student_id}: {str(e)}")

@receiver(post_save, sender=TblStudentBasicInfoApplications)
def update_student_basic_info(sender, instance, created, **kwargs):
    if not created:
        try:
            student_info = TblStudentBasicInfo.objects.get(applicant_id=instance)
            user = User.objects.get(student_id=student_info.student_id)
            
            user.name = f"{instance.first_name} {instance.middle_name or ''} {instance.last_name}".strip()
            user.email = instance.email
            user.save()

            logger.info(f"Updated user information for student ID: {student_info.student_id}")
        except TblStudentBasicInfo.DoesNotExist:
            logger.warning(f"No TblStudentBasicInfo found for applicant ID: {instance.applicant_id}")
        except User.DoesNotExist:
            logger.warning(f"No User found for student ID: {student_info.student_id}")
        except Exception as e:
            logger.error(f"Error updating user information: {str(e)}")