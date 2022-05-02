import generate_arduino_file as gaf

file_name = "welcome.ino"
morse = "-.-- .- -- / ... --- .-.. / ..-. .-. .- ... . / ..-. .. --"

gaf.generate_arduino(file_name, morse)

