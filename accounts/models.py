from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, is_author=False, is_student=False, password=None):
        if not email:
            raise ValueError('Укажите Ваш e-mail')
        
        email = self.normalize_email(email)
        
        if is_author:
            return self.create_author(email, name, password)
        elif is_student:
            return self.create_student(email, name, password)
        else:
            user = self.model(
                email=email,
                name=name,
                is_author=False,
                is_student=False,
                is_staff=True
                )
            user.set_password(password)
            user.save()

            return user


    def create_superuser(self, email, name, password, is_author, is_student):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=name,
            is_staff = True,
            is_superuser = True,
            is_author = False,
            is_student=False
            )
        user.set_password(password)
        user.save()

        return user
    

    def create_author(self, email, name, password):
        author = Author.objects.model(
            email=email,
            name=name,
            is_author = True
            )
        author.set_password(password)
        author.save()

        return author


    def create_student(self, email, name, password):
        student = Student.objects.model(
            email=email,
            name=name,
            is_student = True
            )
        student.set_password(password)
        student.save()

        return student


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_author = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    balance = models.FloatField(default=0, verbose_name='Денежный баланс')

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['name', 'is_author', 'is_student']


class Author(UserAccount):
    first_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Имя")
    last_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Фамилия")
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    country = models.CharField(max_length=155, blank=True, verbose_name="Страна")
    city = models.CharField(max_length=155, null=True, blank=True, verbose_name="Город")
    university = models.CharField(max_length=255, null=True, blank=True, verbose_name="Учебное заведение")
    faculity = models.CharField(max_length=155, null=True, blank=True, verbose_name="Факультет")
    rating = models.PositiveIntegerField(default=0, verbose_name="Рейтинг")
    portfolio = models.ForeignKey('author_attrs.Portfolio', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Портфолио')
    learning_phase = models.ForeignKey('author_attrs.LearningPhase', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Стадия обучения')
    academic_title = models.ForeignKey('author_attrs.AcademicTitle', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Научное звание')
    scientific_rank = models.ForeignKey('author_attrs.ScientificRank', blank=True, null=True, on_delete=models.PROTECT, verbose_name='Ученая степень')
    paper_scientific = models.ManyToManyField('paper_attrs.ScientificArea', blank=True, verbose_name='Области науки')
    paper_subject = models.ManyToManyField('paper_attrs.Subject', blank=True, verbose_name='Предметы')
    paper_type = models.ManyToManyField('paper_attrs.PaperType', blank=True, verbose_name='Типы работ')


class Student(UserAccount):
    favorite_author = models.ManyToManyField('paper_attrs.PaperType', blank=True, verbose_name='Любимый автор')
    # review = models.OneToOneField('author_attrs.Portfolio', blank=True, on_delete=models.PROTECT, parent_link=True, verbose_name='Отзыв')