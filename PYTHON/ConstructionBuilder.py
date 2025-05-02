class ConstructionBuilder:
    def __init__(self, builder_name, buildings_count):
        self.builder_name = builder_name
        self.buildings_count = buildings_count
    def customer_buy_building(self, customer_name, buildings_purchased):
        if (buildings_purchased < 1):
            print (f"Oops..... You can't buy {buildings_purchased} number of buildings")
            return;
        if (self.buildings_count < buildings_purchased):
            print(f"Unfortunately builder named {self.builder_name} has only {self.buildings_count} left at the moment")
            return;
        print (f"Congrats {customer_name} !. You have successfully purchased {buildings_purchased} buildings from {self.builder_name}")
        self.buildings_count -= buildings_purchased

construct_builder_1 = ConstructionBuilder("Zeus", 10)
construct_builder_1.customer_buy_building("Alice", 4)
construct_builder_1.customer_buy_building("Bob", 1)
construct_builder_1.customer_buy_building("Charlie", 2)
construct_builder_1.customer_buy_building("David", 5)
construct_builder_1.customer_buy_building("Elvis", 1)
construct_builder_1.customer_buy_building("Fride", 0)
construct_builder_1.customer_buy_building("Gazlic", -1)