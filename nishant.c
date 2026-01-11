#include<stdio.h>
int main(){
     int pin = 1234;      
    int enteredPin;
    int balance = 1000; 
    int choice, amount;

    printf("Welcome to the ATM Machine!\n");
    printf("Please enter your PIN: ");
    scanf("%d", &enteredPin);

    if (enteredPin != pin) {
        printf("Incorrect PIN. Access denied.\n");
        return 0;
    }

    do {
        printf("\n--- ATM Menu ---\n");
        printf("1. Check Balance\n");
        printf("2. Deposit Money\n");
        printf("3. Withdraw Money\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Your balance is: %d\n", balance);
                break;

            case 2:
                printf("Enter amount to deposit: ");
                scanf("%d", &amount);
                balance += amount;
                printf("Money deposited successfully!\n");
                break;

            case 3:
                printf("Enter amount to withdraw: ");
                scanf("%d", &amount);
                if (amount > balance) {
                    printf("Not enough balance!\n");
                } else {
                    balance -= amount;
                    printf("Please collect your cash.\n");
                }
                break;
                 case 4:
                printf("Thank you for using the ATM!\n");
                break;

            default:
                printf("Invalid choice. Try again.\n");
        }
    } while (choice != 4);

    return 0;
}

