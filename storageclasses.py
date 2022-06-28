
#S3 Storage Class Optimizer by Omar Okasha
#The goal behind this application is to assist clients in determining the most suitable storage class option with data access and resiliency in mind

print("Welcome to the S3 Storage Class")
print("This application is designed to assist you in determining the most cost effective S3 Storage class based on your needs")

#Array is used here to store all the different S3 storage Classes 
storageclasses = ["S3 Standard","S3 Intelligent-Tiering","S3 Standard-Infrequent Access","S3 One Zone-Infrequent Access",\
                  "S3 Glacier Instant Retrieval", "S3 Glacier Flexible Retrieval","S3 Glacier Deep Archive"]


#Client will be prompted to answer several questions, based on the response, the code will only retain relevant Storage Classes in the Array
#This filtering method will lead the client to the most suitable Storage Class

while True:
    frequency = input("Firstly, will you be accessing your data frequently, infrequently or unknown? ").lower()
    if frequency == "frequently":
        storageclasses.remove("S3 Standard-Infrequent Access")
        storageclasses.remove("S3 One Zone-Infrequent Access")
        storageclasses.remove("S3 Glacier Instant Retrieval")
        storageclasses.remove("S3 Glacier Flexible Retrieval")
        storageclasses.remove("S3 Glacier Deep Archive")
        break;
    elif frequency == "unknown":
        quit(print("We recommend you use S3 Intelligent-Tiering"))
    elif frequency == "infrequently":
        storageclasses.remove("S3 Standard")
        break;
    else:
        print("Please enter 'frequently', 'infrequently' or 'unknown' below ")
        

while True:
    backup_type = input("Is this your primary, secondary or archive backup? ").lower()
    if backup_type == "primary":
        if ("S3 One Zone-Infrequent Access") in storageclasses:
            storageclasses.remove("S3 One Zone-Infrequent Access")
        break;
    elif backup_type == "secondary" and frequency == "infrequently":
        quit(print("S3 One Zone-Infrequent Access"))
    elif backup_type == "secondary":
        if ("S3 One Zone-Infrequent Access") in storageclasses:
            storageclasses.remove("S3 One Zone-Infrequent Access")
        if ("S3 Standard-Infrequent Access") in storageclasses:
            storageclasses.remove("S3 Standard-Infrequent Access")
        break;
    elif backup_type == "archive":
        if ("S3 Standard-Infrequent Access") in storageclasses:
            storageclasses.remove("S3 Standard-Infrequent Access")
        break;
    else:
        print("Please enter 'primary', 'secondary' or 'archive' below ")
        

while True:
    storage_duration = input("Will you be storing your data for more than 90 days, Yes or No? ").lower() 
    if storage_duration == "yes":
        if ("S3 Standard") in storageclasses:
            storageclasses.remove("S3 Standard")
        if ("S3 Intelligent-Tiering") in storageclasses:
            storageclasses.remove("S3 Intelligent-Tiering")
        if ("S3 Standard-Infrequent Access") in storageclasses:
            storageclasses.remove("S3 Standard-Infrequent Access")
        if ("S3 One Zone-Infrequent Access") in storageclasses:
            storageclasses.remove("S3 One Zone-Infrequent Access")
        glacier_duration_type = input("Will you be storing the data for more than 180 days, Yes or No? ").lower()
        if glacier_duration_type == "yes":
            if ("S3 Glacier Instant Retrieval") in storageclasses:
                storageclasses.remove("S3 Glacier Instant Retrieval")
            if ("S3 Glacier Flexible Retrieval") in storageclasses:
                storageclasses.remove("S3 Glacier Flexible Retrieval")
                break;
        if glacier_duration_type == "no":
            glacier_retrieval_type = input("When you need your data, will you need access instantly, Yes or No? ").lower()
        if glacier_retrieval_type == "yes":
            if ("S3 Glacier Flexible Retrieval") in storageclasses:
                storageclasses.remove("S3 Glacier Flexible Retrieval")
            if ("S3 Glacier Deep Archive") in storageclasses:
                storageclasses.remove("S3 Glacier Deep Archive")
            break;
        elif glacier_retrieval_type == "no":
            if ("S3 Glacier Instant Retrieval") in storageclasses:
                storageclasses.remove("S3 Glacier Instant Retrieval")
            break;
    if storage_duration == "no":
        if ("S3 Intelligent-Tiering") in storageclasses:
            storageclasses.remove("S3 Intelligent-Tiering")
        break;
    else:
            print("Please enter 'Yes' or 'No' below")
    

print(storageclasses)

