from django.db import models

# Create your models here.























class Book(models.Model):
    category_id = models.ManyToManyField('Category')
    title = models.CharField('Book Name',max_length=127)
    description = models.TextField('Description')
    author = models.ForeignKey('Author',on_delete = models.CASCADE)
    price = models.DecimalField('Price',max_digits=7,decimal_places=2,default =0.00,null=True,blank=True)
    page_count = models.IntegerField('Page Size',default=0,null=True,blank=True)
    cover_image = models.ImageField('Cover Image',upload_to = 'images/book_images/',null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return f'{self.title} {self.author} {self.page_count}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ('title',)


GENDER=(
    (1,'Male'),
    (2,'Female'),
)
class Author(models.Model):
    fullname = models.CharField('Fullname',max_length = 63)
    image = models.ImageField('Author Image',upload_to = 'images/author_images',null=True,blank=True)
    gender = models.IntegerField('Gender',choices=GENDER)
    birthday = models.DateField('Birthday',auto_now=True,null=True,blank=True)
    nationality = models.CharField('Nation',max_length = 63,null=True,blank=True)
    info=models.TextField('Info',default = 'Author info ...')


    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.fullname} {self.birthday} {self.nationality}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ('fullname',)


class Category(models.Model):
    title = models.CharField('Title',max_length = 127)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('title',)









