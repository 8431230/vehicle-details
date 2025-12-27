def vehicle_details(v_ID,name,price,yop):
    result=(
        f"Vehicle ID: {v_ID}\n"
        f"Name: {name}\n"
        f"Price: ${price}\n"
        f"Year of Purchase: {yop}\n" 
              )
    return result
if __name__ == "__main__":
    v_ID="V1234"
    name="car"
    price=24000
    yop=2021
    print(vehicle_details(v_ID, name, price, yop))