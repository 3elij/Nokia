import java.util.Scanner;

public class Nokia {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.println("===NOKIA 5510===");

        while (true) {
            System.out.println("1. Phone book");
            System.out.println("2. Messages");
            System.out.println("3. Chat");
            System.out.println("4. Call register");
            System.out.println("5. Tones");
            System.out.println("6. Settings");
            System.out.println("7. Call divert");
            System.out.println("8. Music");
            System.out.println("9. Games");
            System.out.println("10. Calculator");
            System.out.println("11. Reminders");
            System.out.println("12. Clock");
            System.out.println("13. Profiles");
            System.out.println("14. Services");
            System.out.println("15. SIM services");
            System.out.println("0. Exit");
            System.out.print("Choose a main-menu option: ");
            int menuOption = input.nextInt();

            if (menuOption == 0) {
                break;
            }

            switch (menuOption) {
                case 1 -> {
                    System.out.println("===PHONE BOOK===");
                    while (true) {
                        System.out.println("1. Search");
                        System.out.println("2. Service Nos");
                        System.out.println("3. Add name");
                        System.out.println("4. Erase");
                        System.out.println("5. Edit");
                        System.out.println("6. Copy");
                        System.out.println("7. Assign Tone");
                        System.out.println("8. Send b-card");
                        System.out.println("9. Options");
                        System.out.println("10. Speed Dials");
                        System.out.println("11. Voice tags");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("No contacts saved");
                            case 2 -> System.out.println("Your Network Service Number is XXX-XXX-XXX");
                            case 3 -> System.out.println("Phone book is full");
                            case 4 -> System.out.println("No contacts to erase");
                            case 5 -> System.out.println("No contacts to edit");
                            case 6 -> System.out.println("Under progress");
                            case 7 -> System.out.println("Only Default available at this time");
                            case 8 -> System.out.println("This function is only available with internet access");
                            case 9 -> System.out.println("You are using phone memory");
                            case 10 -> System.out.println("No speed dials set");
                            case 11 -> System.out.println("This function is under construction for now");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 2 -> {
                    System.out.println("===MESSAGES===");
                    while (true) {
                        System.out.println("1. Write messages");
                        System.out.println("2. Inbox");
                        System.out.println("3. Outbox");
                        System.out.println("4. Picture messages");
                        System.out.println("5. Templates");
                        System.out.println("6. Smileys");
                        System.out.println("7. Message settings");
                        System.out.println("8. Info service");
                        System.out.println("9. Voice mailbox number");
                        System.out.println("10. Service command editor");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("Message sent");
                            case 2 -> System.out.println("No one wants to talk to you");
                            case 3 -> System.out.println("Your outbox is empty");
                            case 4 -> System.out.println("Nobody wants to send you pictures");
                            case 5 -> System.out.println("Since nobody is texting you, you dont need these");
                            case 6 -> System.out.println(":-), :-( , ;-), :-<, :-> ");
                            case 7 -> System.out.println("Your network message centre number is +234803000000");
                            case 8 -> System.out.println("The weather today is sunny");
                            case 9 -> System.out.println("Call 121 to access your voicemail");
                            case 10 -> System.out.println("Dial *456# to check your balance");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 3 -> {
                    System.out.println("===CHAT===");
                    System.out.println("Chat is not available");
                }
                case 4 -> {
                    System.out.println("===CALL REGISTER===");
                    while (true) {
                        System.out.println("1. Make calls");
                        System.out.println("2. Call Log");
                        System.out.println("3. Erase Call log");
                        System.out.println("4. Show call duration");
                        System.out.println("5. Show call costs");
                        System.out.println("6. Airtime Balance");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("Calling.... No internet access");
                            case 2 -> System.out.println("You have no calls");
                            case 3 -> System.out.println("Call log erased");
                            case 4 -> System.out.println("Your calls lasted an average of 4 minutes");
                            case 5 -> System.out.println("Your calls cost $1 per minute");
                            case 6 -> System.out.println("You have $0.0 left");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 5 -> {
                    System.out.println("===TONES===");
                    while (true) {
                        System.out.println("1. Ringing tone");
                        System.out.println("2. Incoming call alert");
                        System.out.println("3. Message alert tone");
                        System.out.println("4. Keypad tones");
                        System.out.println("5. Warning tones");
                        System.out.println("6. Vibrating alert");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("The ringtone is Nokia Tune");
                            case 2 -> System.out.println("The phone will ring");
                            case 3 -> System.out.println("The alert for a new message is a chime");
                            case 4 -> System.out.println("Keypad tones are on");
                            case 5 -> System.out.println("Warning tones are on");
                            case 6 -> System.out.println("Vibrate is on");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 6 -> {
                    System.out.println("===SETTINGS===");
                    while (true) {
                        System.out.println("1. Call settings");
                        System.out.println("2. Phone settings");
                        System.out.println("3. Security settings");
                        System.out.println("4. Restore factory settings");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("Automatic redial is on");
                            case 2 -> System.out.println("Language is English");
                            case 3 -> System.out.println("PIN verification is off");
                            case 4 -> System.out.println("All information has been cleared from the phone");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 7 -> {
                    System.out.println("===CALL DIVERT===");
                    System.out.println("Call divert isn't supported on this device");
                }
                case 8 -> {
                    System.out.println("===MUSIC===");
                    while (true) {
                        System.out.println("1. Music player");
                        System.out.println("2. Radio");
                        System.out.println("3. Recorder");
                        System.out.println("4. Track list");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("Music player isnt supported on this device");
                            case 2 -> System.out.println("Radio isnt supported on this device");
                            case 3 -> System.out.println("Recorder isn't supported on this device");
                            case 4 -> System.out.println("This function isn't supported on this device");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 9 -> {
                    System.out.println("===GAMES===");
                    while (true) {
                        System.out.println("1. Snake II");
                        System.out.println("2. Space Impact");
                        System.out.println("3. Bumper");
                        System.out.println("4. Bantumi");
                        System.out.println("5. Pairs II");
                        System.out.println("0. Back");
                        System.out.print("Choose an option: ");
                        int option = input.nextInt();

                        if (option == 0) {
                            break;
                        }

                        switch (option) {
                            case 1 -> System.out.println("Snake II needs to be downloaded");
                            case 2 -> System.out.println("Space Impact needs to be downloaded");
                            case 3 -> System.out.println("Bumper needs to be downloaded");
                            case 4 -> System.out.println("Bantumi needs to be downloaded");
                            case 5 -> System.out.println("Pairs II needs to be downloaded");
                            default -> System.out.println("Invalid option");
                        }
                    }
                }
                case 10 -> {
                    System.out.println("===CALCULATOR===");
                    System.out.print("First number: ");
                    double first = input.nextDouble();
                    System.out.print("Operator (+, -, *, /): ");
                    String operator = input.next();
                    System.out.print("Second number: ");
                    double second = input.nextDouble();

                    switch (operator) {
                        case "+" -> System.out.println("= " + (first + second));
                        case "-" -> System.out.println("= " + (first - second));
                        case "*" -> System.out.println("= " + (first * second));
                        case "/" -> System.out.println("= " + (first / second));
                        default -> System.out.println("Unknown operator");
                    }
                }
                case 11 -> {
                    System.out.println("===REMINDERS===");
                    System.out.println("You have no reminders");
                }
                case 12 -> {
                    System.out.println("===CLOCK===");
                    System.out.println("Clock is still under construction");
                }
                case 13 -> {
                    System.out.println("===PROFILES===");
                    System.out.println("There is only one profile on this device");
                }
                case 14 -> {
                    System.out.println("===SERVICES===");
                    System.out.println("You do not have access to the internet");
                }
                case 15 -> {
                    System.out.println("===SIM SERVICES===");
                    System.out.println("You need internet access to access this function");
                }
                default -> System.out.println("Invalid option");
            }
        }

        System.out.println("===Thank you for using NOKIA 5510!===");
    }
}