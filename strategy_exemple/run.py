from src import Context, ConcreteStrategyA, ConcreteStrategyB

if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    data = ["apple", "banana", "cherry", "dates", "eggplant"]
    
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic(data)
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic(data)
    print()

    print("Client: Strategy is set to reverse sorting, but the Context data is None.")
    context.strategy = ConcreteStrategyB()
    context.do_some_business_logic()