from .models import InfoModel, SkillCategoryModel, ReviewModel


def get_current_info():
    return InfoModel.objects.order_by("-updated_at").first()


def get_skill_categories():
    return SkillCategoryModel.objects.all()


def get_reviews():
    return ReviewModel.objects.all().order_by("-created_at")[:4]

