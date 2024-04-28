
struct Employee {
    1: string name,
    2: string position,
    3: string email,
    4: string phone
}

struct Department {
    1: string name,
    2: string head,
    3: list<Employee> employees
}


struct Location {
    1: string address,
    2: string city,
    3: string state,
    4: string zip,
    5: string country
}

struct Product {
    1: string name,
    2: string type,
    3: double price
}

struct Company {
    1: string name,
    2: Location location,
    3: list<Department> departments,
    4: list<Product> products,
    5: double revenue,
    6: string founded
}
