from tkinter import *
#from tkinter.ttk import *
import os
import webbrowser

from numpy.distutils.fcompiler import none


def dockerManuall():
    # first we have to create the volume
    os.system('docker volume create {}'.format(createVol.get()))
    os.system('docker volume create {}'.format(createVolWordpress.get()))
    os.system('docker run -dit -e MYSQL_ROOT_PASSWORD={} -e MYSQL_USER={} -e MYSQL_PASSWORD={} -e MYSQL_DATABASE={} -v  {}:/var/lib/mysql --name {} mysql:5.7'.format(mysqlRootPassword.get(),mySQLUsername.get(),mySQLPassword.get(),mySQLDatabase.get(),createVol.get(),mysqlContainerName.get()))
    os.system('docker run -dit -e WORDPRESS_DB_HOST={} -e WORDPRESS_DB_USER={} -e WORDPRESS_DB_PASSWORD={} -e WORDPRESS_DB_NAME={} -v {}:/var/www/html --name {} -p {}:{} --link {} wordpress:5.1'.format(mysqlContainerName.get(),mySQLUsername.get(),mySQLPassword.get(),mySQLDatabase.get(),createVolWordpress.get(),wordpressContainerName.get(),int(portNumber.get()),int(portNumber2.get()),mysqlContainerName.get()))
    webbrowser.open_new_tab('192.168.1.108:8080')
    print('docker run -dit -e MYSQL_ROOT_PASSWORD={} -e MYSQL_USER={} -e MYSQL_PASSWORD={} -e MYSQL_DATABASE={} -v  {}:/var/lib/mysql --name {} mysql:5.7'.format(mysqlRootPassword.get(),mySQLUsername.get(),mySQLPassword.get(),mySQLDatabase.get(),createVol.get(),mysqlContainerName.get()))
    print('docker run -dit -e WORDPRESS_DB_HOST={} -e WORDPRESS_DB_USER={} -e WORDPRESS_DB_PASSWORD={} -e WORDPRESS_DB_NAME={} -v {}:/var/www/html --name {} -p {}:{}  --link {} wordpress:5.1'.format(mysqlContainerName.get(),mySQLUsername.get(),mySQLPassword.get(),mySQLDatabase.get(),createVolWordpress.get(),wordpressContainerName.get(),int(portNumber.get()),int(portNumber2.get()),mysqlContainerName.get()))

def dockerCompose():
    os.system('docker-compose up')
    webbrowser.open_new_tab('192.168.1.108:8080') or webbrowser.open_new('192.168.1.108:8080')


if __name__ == '__main__':
    screen1 = Tk()
    screen1.title("Project02")
    screen1.geometry('1024x1000')
    Label(screen1,text="Docker Project",font=('Arial',50)).grid(column = 3,row=1)

    Label(screen1,text="Manual Configuration",background='red',foreground='white',font=('Arial',15)).grid(column = 3, row = 4, padx=12, pady=25)

    # create volume for Wordpress
    Label(screen1, text="Enter Volume name for wordpress : ",font=('Arial',15)).grid(column=2, row=5)

    createVolWordpress = Entry(screen1, width=27,font=('Arial',15))
    createVolWordpress.insert(0, 'Enter Vol name for wordpress')
    createVolWordpress.grid(column=3, row=5, padx=10, pady=10,ipady=5)

    # create volume for mysql
    Label(screen1,text="Enter Volume name for MYSQL : ",font=('Arial',15)).grid(column = 2,row=6)

    createVol = Entry(screen1,width=27,font=('Arial',15))
    createVol.insert(0,'Enter Vol name for mysql')
    createVol.grid(column = 3,row=6,padx=10,pady=10,ipady=5)

    # Database Container name
    Label(screen1, text="Enter Database Container name (It will be your host name) : ",font=('Arial',15)).grid(column=2, row=7)

    mysqlContainerName = Entry(screen1, width=27,font=('Arial',15))
    mysqlContainerName.insert(0, 'Ex. dbos')
    mysqlContainerName.grid(column=3, row=7, padx=10, pady=25,ipady=5)

    # MySQL root password
    Label(screen1, text="Mysql root password (MYSQL_ROOT_PASSWORD) : ",font=('Arial',15)).grid(column=2, row=8)

    mysqlRootPassword = Entry(screen1, width=27,font=('Arial',15))
    mysqlRootPassword.insert(0, 'Ex. mydbos')
    mysqlRootPassword.grid(column=3, row=8, padx=10, pady=10, ipady=5)

    # MySQL_USERNAME
    Label(screen1, text="Enter username (MYSQL_USERNAME) : ",font=('Arial',15)).grid(column=2, row=9)

    mySQLUsername = Entry(screen1, width=27,font=('Arial',15))
    mySQLUsername.insert(0, 'Ex. ashu')
    mySQLUsername.grid(column=3, row=9, padx=10, pady=10,ipady=5)

    # MySQL_PASSWORD
    Label(screen1, text="Enter password (MYSQL_PASSWORD) : ",font=('Arial',15)).grid(column=2, row=10)

    mySQLPassword = Entry(screen1, width=27,font=('Arial',15))
    mySQLPassword.insert(0, 'Ex. ashu@1999')
    mySQLPassword.grid(column=3, row=10, padx=10, pady=10,ipady=5)

    # # MySQL_HOST
    # Label(screen1, text="Enter host (MYSQL_HOST) : ").grid(column=2, row=11)
    #
    # mySQLHost = Entry(screen1, width=27)
    # mySQLHost.insert(0, 'Ex. localhost')
    # mySQLHost.grid(column=3, row=11, padx=10, pady=25)

    # MySQL_DATABASE_NAME
    Label(screen1, text="Enter Database name (MYSQL_DATABASE_NAME) : ",font=('Arial',15)).grid(column=2, row=12)

    mySQLDatabase = Entry(screen1,width=30,font=('Arial',15) )
    mySQLDatabase.insert(0, 'Ex. myDB')
    mySQLDatabase.grid(column=3, row=12, padx=10, pady=10,ipady=5)

    # Wordpress Container name
    Label(screen1, text="Enter Wordpress Container Name : ",font=('Arial',15)).grid(column=2, row=13)

    wordpressContainerName = Entry(screen1, width=27,font=('Arial',15))
    wordpressContainerName.insert(0, 'Ex. myWebsite01')
    wordpressContainerName.grid(column=3, row=13, padx=12, pady=10,ipady=5)

    # Port Number
    Label(screen1, text="Port Number : ",font=('Arial',15)).grid(column=2, row=15)

    portNumber = Entry(screen1, width=27,font=('Arial',15))
    portNumber.insert(0, 'Ex. 8080')
    portNumber.grid(column=3, row=15, padx=12, pady=10,ipady=5)

    Label(screen1,text=":",font=('Arial',15)).grid(column = 4, row = 15)

    portNumber2 = Entry(screen1, width=27,font=('Arial',15))
    portNumber2.insert(0, 'Ex. 80')
    portNumber2.grid(column=5, row=15, padx=12, pady=10,ipady=5)

    Button(screen1, text="Submit", command=dockerManuall, fg="green", bg="white",font=('Arial',15)).grid(column=3, row=16,ipady=5)

    # One CLick auto configure

    Label(screen1,text="One click and Auto Configure using docker compose file",background='green',foreground='white',font=('Arial',15)).grid(column = 3, row = 17, padx=12, pady=25)

    btn1 = Button(screen1, text="Start", command=dockerCompose, fg="green", bg="white",font=('Arial',15))
    btn1.grid(column=3, row=18,padx=15,pady=10,ipady=5)




    screen1.mainloop()




