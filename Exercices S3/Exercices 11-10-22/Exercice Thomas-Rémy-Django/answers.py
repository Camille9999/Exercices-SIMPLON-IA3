def price_filter_good(data):
    result = ""
    for company in data:
        if company["price"] > 500:
            result += f'ANS: Company name : {company["company_name"]}, price : {company["price"]}'
    print(result)


def find_partners_good():
    return ["Adobe", "Amazon", "Apple", "Borland", "Cakewalk", "Chami",
            "Finale", "Google", "Lavasoft", "Microsoft", "Sibelius", "Yahoo"]


def average_price_good():
    return 522

def companies_stock_good():
    return [{'company_name': 'Adobe', 'stock': 19198.0}, {'company_name': 'Amazon', 'stock': 22556.0}, {'company_name': 'Apple', 'stock': 18295.5}, {'company_name': 'Borland', 'stock': 20505.5}, {'company_name': 'Cakewalk', 'stock': 25456.0}, {'company_name': 'Chami', 'stock': 24803.5}, {'company_name': 'Finale', 'stock': 25045.0}, {'company_name': 'Google', 'stock': 15633.0}, {'company_name': 'Lavasoft', 'stock': 23557.0}, {'company_name': 'Microsoft', 'stock': 22307.5}, {'company_name': 'Sibelius', 'stock': 21629.0}, {'company_name': 'Yahoo', 'stock': 17201.5}]
