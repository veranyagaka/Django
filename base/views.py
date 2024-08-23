from django.shortcuts import render

# Create your views here.
'''
Django
- Serializers
- JWT
- CSRF
- CORS
- ORM
- Asynchronous
'''
import asyncio
import aiohttp

async def fetch_data(session, url):
    async with session.get(url) as response:
        data = await response.text()
        print(f"Fetched data from {url}")
        return data

async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/todos/2',
        'https://jsonplaceholder.typicode.com/todos/3'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for url in urls]
        results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

# Running the asynchronous main function
asyncio.run(main())

'''
ORM
- Object Relational Mapping
1. Defining models
    -models.Model: Charfield, EmailField, DateField, DecimalField

2. Creating Records
creating instance and saving it:
employee=Employee(first_name=''John....)
employee.save()
OR
employee=Employee.object.create(first_name='John'....)

2b. Reading records
v=Employee.objects.all()
one= Employee.objects.get(id=1)
filter=Employee.objects.filter(first_name='John')
one+filter= Employee.objects.get(email="meow@gmail.com")

2c. Updating records
save method: retrieve, update and then save
OR at the same time ----.update()
Employee.objects.filter(first_name='John').update(first_name='Jane')

2d, Deleting Records
i) .delete() method
2. retrieve, employee.delete()

3. QuerySet Methods

£a. Filtering using Q objects - OR conditions
£b.Excluding - .exclude()

£c. Ordering
Employee.objects.order_by('first_name')
Employee.objects.order_by('-first_name')

Aggregation and Annotation
Employee.objects.aggregate(Avg('salary'))
Employee.objects.annotate(Count('salary'))
Employee.objects.annotate(Max('salary'))

4. FK and Related Models
1-1 relationship
1-Many
Many-Many

5. Migrations

6. Advanced
a) Custom Managerrs
class em(models.Manager):
    def high(self):
    return 
class Employee
    employee=em()

b) Inheitance

'''