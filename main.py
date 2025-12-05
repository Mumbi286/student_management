import click
from database import Database
from student import Student

Database.initialise()

@click.group()
def cli():
    """Student Management System"""
    pass
# Adds a new student
@cli.command()
@click.option("--name", prompt="Name")
@click.option("--course", prompt="Course")
@click.option("--mobile", prompt = "Mobile")

def add(name, course,mobile):
     try:
        s = Student()
        s.set_name(input("Name: "))
        s.set_course(input("Course: "))
        s.set_mobile(input("Mobile: "))
        s.save()
        print("Added Successfully!")
     except Exception as e:
       click.echo(f"Error: {e}")

# view students 
@cli.command()
def view(): 
    """View Students """
    try:
        rows = Student.get_all()
        if not rows:
            click.echo("Student not available.")
            return

        click.echo("ID | Name | Course | Mobile")
        for r in rows:
            click.echo(f"{r[0]} | {r[1]} | {r[2]} |{r[3]}")
    except Exception as e:
            click.echo(f"Error: {e}")

#update student   
@cli.command()
@click.option("--id", prompt = "Student ID")
@click.option("--name", prompt="New Name")
@click.option("--course", prompt="New Course")
@click.option("--mobile", prompt="New Mobile") 
def update(id, name, course, mobile):
    """Update student details"""
    try:
       student_id = input("Student Updated: ")
       click.echo("Updated Successful!")

    except Exception as e:
        click.echo(f"Error: {e}")

# DELETE STUDENT
@click.command()
@click.option("--id", prompt="Student ID")
def delete(id):
    """Delete a student"""
    try:
        student.delete(id)
        click.echo("Deleted succeful!")
    except Expection as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    cli()

            


            
            