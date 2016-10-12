from celery.decorators import task

@task(name="suma_dos_numeros")
def add(x,y):

	return x + y