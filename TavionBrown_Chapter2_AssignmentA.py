# This program checks for spam in email messages and allows multiple attempts

# List of 30 common spam words and phrases
spam_words = [
    'credit', 'apply online', 'additional income', 'big bucks', 'urgent', 
    'can we have a minute of your time', 'lowest price', 'claim now', 'prince', 'fee', 'no experience', 
    'gimmick', 'investment', 'spam', 'vacation', 'winner', 'congratulations', 
    'dear friend', 'no questions asked', 'offer', 'online pharmacy', 'please read', 
    'instant access', 'free', 'guarantee', 'insurance', 'serious', 'your income', 
    'work from home', 'expire'
]

# Determing how the scores will be
def calculate_spam_score(message):
    spam_score = 0
    detected_keywords = []

    for word in spam_words:
        count = message.count(word)
        if count > 0:
            spam_score += count
            detected_keywords.append((word, count))

    return spam_score, detected_keywords

# The score on how likely it is a spam
def determine_spam_likelihood(score):
    if score == 0:
        return "Not a spam"
    elif score <= 5:
        return "Unlikely to be a spam"
    elif score <= 15:
        return "There's a possiblity that this is a spam"
    elif score <= 25:
        return "Likely to be a spam"
    else:
        return "Highly likely to be a spam"

def main():
    total_spam_score = 0

    while True:
        # Input: email message
        message = input("Enter the email message (or type 'exit' to finish):\n").lower()
        
        if message == 'exit':
            break

        # Calculate spam score and detected keywords
        spam_score, detected_keywords = calculate_spam_score(message)
        total_spam_score += spam_score

        # Determine likelihood of spam
        likelihood = determine_spam_likelihood(total_spam_score)

        # Display results
        print("\nCurrent Spam Score:", spam_score)
        print("Total Spam Score:", total_spam_score)
        print("Likelihood of being spam:", likelihood)
        if detected_keywords:
            print("Detected spam words/phrases in this message:")
            for word, count in detected_keywords:
                print(f" - {word}: {count} time(s)")

        print("\n") 

    print("Final Total Spam Score:", total_spam_score)
    print("Final Likelihood of being spam:", determine_spam_likelihood(total_spam_score))

if __name__ == "__main__":
    main()
