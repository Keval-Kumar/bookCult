from django.db import models

# Create your models here.
class Members(models.Model):
    name  = models.CharField(max_length=100)
    usn = models.CharField(max_length=15)
    branch_choices=[
        ('CSE-AIML','CSE-AIML'),
        ('AI & DS','AI & DS'),
        ('ISE','ISE'),
        ('CSE','CSE'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('ETE','ETE'),
        ('EIE','EIE'),
        ('MECH','MECH'),
        ('CIVIL','CIVIL'),
        ('BIOTECH','BIOTECH'),
        ('CHEMICAL','CHEMICAL'),
        ('IEM','IEM'),
    ]
    year_choices=[
        ('1st year','1st year'),
        ('2st year','2st year'),
        ('3st year','3st year'),
        ('4st year','4st year'),
    ]
    year = models.CharField(choices=year_choices)
    branch = models.CharField(choices=branch_choices)

class books(models.Model):
    bookname  = models.CharField(max_length=100)
    bookid = models.CharField(max_length=15,primary_key=True)
    price  = models.DecimalField(max_digits=5,decimal_places=3)

class blogs(models.Model):
    name  = models.CharField(max_length=100)
    bookid = models.ForeignKey(
        books,
        on_delete=models.CASCADE,
        related_name='main_review'
    )
    content  = models.TextField()
    usn = models.ForeignKey(
        Members,
        on_delete=models.CASCADE,
        related_name='member_usn'
    )


class author(models.Model):
    name  = models.CharField(max_length=100)
    authorid = models.CharField(max_length=15,primary_key=True)
    
class bookauthor(models.Model):
    authorid  = models.ForeignKey(
          author,
          on_delete=models.CASCADE,
          related_name="author"
    )

    bookid = models.ForeignKey(
          books,
          on_delete=models.CASCADE,
          related_name='book'
        )
    pk = models.CompositePrimaryKey("bookid", "authorid")

class bookurl(models.Model):
    bookid  = models.ForeignKey(
          books,
          on_delete=models.CASCADE,
          related_name='book2'
    )
    bookurl = models.URLField()
    pk = models.CompositePrimaryKey("bookid", "bookurl")
    

class likes(models.Model):
    usn  = models.ForeignKey(
          Members,
          on_delete=models.CASCADE,
          related_name='members1'
    )
    blogs = models.ForeignKey(
          blogs,
          on_delete=models.CASCADE,
          related_name='blog1'
    )
    pk = models.CompositePrimaryKey("usn", "blogs")

class comments(models.Model):
    usn  = models.ForeignKey(
          Members,
          on_delete=models.CASCADE,
          related_name='member2'
    )
    blogs = models.ForeignKey(
          blogs,
          on_delete=models.CASCADE,
          related_name='blog2'
    )
    # comment id = integer.autofield

class dislikes(models.Model):
    usn  = models.ForeignKey(
          Members,
          on_delete=models.CASCADE,
          related_name='members3'
    )
    blogs = models.ForeignKey(
          blogs,
          on_delete=models.CASCADE,
          related_name='blogs3'
    )
    pk = models.CompositePrimaryKey("usn", "blogs")