Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import json
>>> x={
	"name":"Aishwarya",
	"age": 19,
	"college": "SRM University, Ramapuram",
	"Interest": "AI AND Web Development",
	"Hobbys": "DIY and Handlettering",
	"pets": "Fishes and Birds"
}
>>> print(json.dumps(x))
{"name": "Aishwarya", "age": 19, "college": "SRM University, Ramapuram", "Interest": "AI AND Web Development", "Hobbys": "DIY and Handlettering", "pets": "Fishes and Birds"}
>>> 
