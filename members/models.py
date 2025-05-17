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

class books(models.model):
    bookname  = models.CharField(max_length=100)
    bookid = models.CharField(max_length=15,primary_key=True)
    price  = models.DecimalField()

class blogs(models.model):
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


class author(models.model):
    name  = models.CharField(max_length=100)
    authorid = models.CharField(max_length=15,primary_key=True)
    
class bookauthor(models.model):
    authorid  = models.ForeignKey(
          author,
          on_delete=models.CASCADE,
          related_name='authorid of book author'
    )

    bookid = models.ForeignKey(
          books,
          on_delete=models.CASCADE,
          related_name='bookid of bookauthor'
        )
    pk = models.CompositePrimaryKey("bookid", "authorid")

class bookurl(models.model):
    bookid  = models.ForeignKey(
          books,
          on_delete=models.CASCADE,
          related_name='bookid of bookid'
    )
    bookurl = models.ForeignKey(
          on_delete=models.CASCADE,
          related_name='bookurl of bookid'
    )
    pk = models.CompositePrimaryKey("bookid", "bookurl")
    

class likes(models.model):
    usn  = models.ForeignKey(
          Members,
          on_delete=models.CASCADE,
          related_name='usn of likes'
    )
    blogs = models.ForeignKey(
          blogs,
          on_delete=models.CASCADE,
          related_name='blogs of likes'
    )
    pk = models.CompositePrimaryKey("usn", "blogs")

class comments(models.model):
    usn  = models.ForeignKey(
          Members,
          on_delete=models.CASCADE,
          related_name='usn of comments'
    )
    blogs = models.ForeignKey(
          blogs,
          on_delete=models.CASCADE,
          related_name='blogs of comments'
    )
    # comment id = integer.autofield

class dislikes(models.model):
    usn  = models.ForeignKey(
          Members,
          on_delete=models.CASCADE,
          related_name='usn of comments'
    )
    blogs = models.ForeignKey(
          blogs,
          on_delete=models.CASCADE,
          related_name='blogs of comments'
    )
    pk = models.CompositePrimaryKey("usn", "blogs")