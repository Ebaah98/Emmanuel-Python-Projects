def main():
    services = []  # create an empty list of services

    # add services to the list using append or insert
    services.append('S3')
    services.append('Lambda')
    services.insert(1, 'EC2')
    services.append('RDS')

    # print the list and its length
    print("Services: ", services)
    print("Number of services: ", len(services))

    # remove two specific services from the list by name or by index
    services.remove('Lambda')
    del services[0]

    # print the new list and its length
    print("Updated services: ", services)
    print("Number of updated services: ", len(services))


main()  # call the main function explicitly
