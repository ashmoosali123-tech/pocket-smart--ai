"""Generate a synthetic expense dataset for POCKETsmart AI (reproducible, seed=42)."""
import random, csv
from datetime import date, timedelta
from pathlib import Path

random.seed(42)
CATS = {
 "Food": (["Swiggy","Zomato","Dominos pizza","McDonalds","Cafe Coffee Day","Starbucks","Local restaurant","Biryani house","Grocery store","BigBasket order","Vegetable market","Bakery","Tea stall","Canteen lunch","Milk and eggs"], (60, 900)),
 "Transport": (["Uber ride","Ola cab","Rapido bike","Metro card recharge","Bus pass","Petrol","Diesel fill","Auto rickshaw","Train ticket IRCTC","Parking fee","Toll charge","Bike service","FASTag recharge"], (20, 1500)),
 "Shopping": (["Amazon order","Flipkart purchase","Myntra clothes","Ajio shirt","Nike shoes","Headphones","Phone cover","Backpack","Watch","Books from bookstore","Jeans","Gift for friend","Meesho order"], (200, 5000)),
 "Bills": (["Electricity bill","Water bill","Wifi bill","Mobile recharge","Airtel postpaid","Jio recharge","Gas cylinder","House rent","Hostel fees","Insurance premium","DTH recharge","Loan EMI"], (150, 12000)),
 "Entertainment": (["Netflix subscription","Spotify premium","Movie tickets PVR","Amazon Prime","Hotstar plan","Gaming top-up","Concert pass","Bowling with friends","YouTube premium","Theme park entry","Book my show"], (100, 2500)),
 "Health": (["Pharmacy medicines","Doctor consultation","Apollo pharmacy","Lab test","Gym membership","Dental checkup","Eye test and glasses","Vitamins","Hospital bill","Yoga class","Health insurance"], (100, 4000)),
 "Other": (["ATM withdrawal","Donation","Stationery","Photocopy and printing","Laundry","Haircut salon","Courier charges","Online course fee","Pet food","Repair work","Miscellaneous"], (30, 2000)),
}
rows = []
start = date(2026, 1, 1)
for _ in range(420):
    cat = random.choices(list(CATS), weights=[28, 16, 14, 12, 10, 8, 12])[0]
    names, (lo, hi) = CATS[cat]
    desc = random.choice(names)
    if random.random() < 0.3:
        desc += random.choice([" upi", " payment", " today", " online", " card"])
    rows.append([(start + timedelta(days=random.randint(0, 239))).isoformat(),
                 desc, round(random.uniform(lo, hi) / 10) * 10, cat])
rows.sort()
out = Path(__file__).parent / "raw/expenses_dataset.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["date","description","amount","category"]); w.writerows(rows)
print(len(rows), "rows ->", out)
