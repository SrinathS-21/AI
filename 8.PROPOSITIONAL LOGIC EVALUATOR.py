def evaluate(exp):
    result = eval(exp)
    if result:
        print("The proposition is True.")
    else:
        print("The proposition is False.")

def main():
    print("Enter your expression:")
    exp = input().strip()
    evaluate(exp)

if __name__ == "__main__":
    main()
