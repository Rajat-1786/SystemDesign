from ttypes import Company, Location, Department, Employee, Product

def convert(inputJson):

    # Create an instance of the Company struct and populate it with data
    company = Company()
    company.name = inputJson['company']['name']
    company.revenue = inputJson['company']['revenue']
    company.founded = inputJson['company']['founded']
    
    # Populate location
    location = Location()
    location.address = inputJson['company']['location']['address']
    location.city = inputJson['company']['location']['city']
    location.state = inputJson['company']['location']['state']
    location.zip = inputJson['company']['location']['zip']
    location.country = inputJson['company']['location']['country']

    company.location = location


    departments = []
    for itr in inputJson['company']['departments']:
        department = Department()
        department.name = itr['name']
        department.head = itr['head']
        employees = []
        for e in itr['employees']:
            employee = Employee()
            employee.name = e['name']
            employee.position = e['position']
            employee.email = e['email']
            employee.phone = e['phone']
            employees.append(employee)

        department.employees = employees
        departments.append(department)
    
    company.departments = departments
    
    products =[]

    for itr in inputJson['company']['products']:
        product = Product()
        product.name = itr['name']
        product.type = itr['type']
        product.price = itr['price']
        products.append(product)

    company.products = products

    return company