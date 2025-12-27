from vehicle import vehicle_details
def test_vehicle_details():
    v_ID="V1234"
    name="car"
    price=24000
    yop=2021
    expected_output=(
        "Vehicle ID: V1234\n"
        "Name: car\n"
        "Price: $24000\n"
        "Year of Purchase: 2021\n"
    )
    assert vehicle_details(v_ID, name, price, yop) == expected_output