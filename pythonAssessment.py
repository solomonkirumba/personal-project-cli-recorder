"""
pythonAssessment.py
Text Analysis Tool for News Articles
This script performs various NLP tasks on a news article including word counting,
paragraph counting, sentence counting, and more.
Student Name: [Your Name]
Date: [Current Date]
"""

# The article text from ACME Inc.
ARTICLE_TEXT = """
ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the "Apple Pie Master," this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. "This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results," Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, "The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one."

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. "We want to cater to all taste preferences, from the traditional to the adventurous," said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master's environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. "Sustainability is at the core of all our product designs," emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, "It's like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings."

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. "The Apple Pie Master is just the beginning," said CEO Jane Doe. "We're exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking."

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""

def count_specific_word(text, search_word):

    # Convert both text and search word to lowercase for case-insensitive comparison
    text_lower = text.lower()
    search_word_lower = search_word.lower()
    
    # Split the text into words
    words = text_lower.split()
    
    # Count occurrences using a for loop
    count = 0
    for word in words:
        # Remove punctuation from the word for accurate counting
        clean_word = word.strip('.,!?;:"\'()[]{}')
        if clean_word == search_word_lower:
            count += 1
    
    return count

def identify_most_common_word(text):
  
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Clean words from punctuation
    clean_words = []
    for word in words:
        clean_word = word.strip('.,!?;:"\'()[]{}')
        if clean_word:  # Only add non-empty strings
            clean_words.append(clean_word)
    
    # Create a dictionary to store word frequencies
    word_count = {}
    for word in clean_words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Find the word with maximum frequency
    if not word_count:
        return ""
    
    max_count = 0
    most_common = ""
    
    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common = word
    
    return most_common

def calculate_average_word_length(text):
   
    # Split into words
    words = text.split()
    
    # Clean words from punctuation
    clean_words = []
    for word in words:
        clean_word = word.strip('.,!?;:"\'()[]{}')
        if clean_word:  # Only add non-empty strings
            clean_words.append(clean_word)
    
    # Calculate total characters and word count
    if not clean_words:
        return 0.0
    
    total_chars = 0
    for word in clean_words:
        total_chars += len(word)
    
    # Calculate average
    average = total_chars / len(clean_words)
    return round(average, 2)

def count_paragraphs(text):
  
    # Split text by newlines
    lines = text.split('\n')
    
    paragraph_count = 0
    in_paragraph = False
    
    for line in lines:
        # Check if line is not just whitespace
        if line.strip():
            if not in_paragraph:
                paragraph_count += 1
                in_paragraph = True
        else:
            in_paragraph = False
    
    return paragraph_count

def count_sentences(text):
 
    import re
    
    # Split on sentence boundaries (.!?) and filter out empty strings
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    
    return len(sentences)

def demonstrate_for_loop_usage(text):

    print("\n" + "="*50)
    print("FOR LOOP DEMONSTRATION: Top 5 Most Common Words")
    print("="*50)
    
    # Using a for loop to analyze word frequencies
    words = text.lower().split()
    word_counts = {}
    
    # For loop to count word frequencies
    for word in words:
        clean_word = word.strip('.,!?;:"\'()[]{}')
        if clean_word and len(clean_word) > 3:  # Skip short words for better analysis
            word_counts[clean_word] = word_counts.get(clean_word, 0) + 1
    
    # Sort and display top 5
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Another for loop to display results
    for i, (word, count) in enumerate(sorted_words[:5], 1):
        print(f"  {i}. '{word}' - appears {count} times")

def demonstrate_while_loop_usage():
    """
    Helper function to demonstrate while loop usage through an interactive menu.
    """
    print("\n" + "="*50)
    print("WHILE LOOP DEMONSTRATION: Interactive Menu System")
    print("="*50)
    print("This menu will continue running until you choose to exit.")
    
    attempts = 0
    # While loop for interactive menu
    while attempts < 3:  # Limit to 3 attempts for demonstration
        print(f"\nAttempt {attempts + 1} of 3")
        print("1. View article summary")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")
        
        # If/else statement inside while loop
        if choice == '1':
            print("\nArticle: ACME Inc. Unveils Revolutionary Apple Pie Machine")
            print("This article discusses the launch of a new automated baking device")
            print("that uses AI technology to make apple pies.")
            break
        elif choice == '2':
            print("Exiting menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            attempts += 1
            
            # Nested if statement
            if attempts >= 3:
                print("Maximum attempts reached. Exiting menu.")
                break

def main():
    """
    Main function to run the text analysis
    """
    print("="*60)
    print("NEWS ARTICLE ANALYSIS TOOL")
    print("Analyzing: ACME Inc. Unveils Revolutionary Apple Pie Machine")
    print("="*60)
    
    # Store the article text in a variable
    article = ARTICLE_TEXT
    
    # Display basic article information
    print(f"\nArticle length: {len(article)} characters")
    print(f"Number of lines: {len(article.split(chr(10)))}")
    
    # Use a while loop for interactive menu (fulfills while loop requirement)
    while True:
        print("\n" + "-"*40)
        print("MAIN MENU")
        print("-"*40)
        print("Select an analysis option:")
        print("1. Count specific word occurrences")
        print("2. Identify most common word")
        print("3. Calculate average word length")
        print("4. Count number of paragraphs")
        print("5. Count number of sentences")
        print("6. Run complete analysis")
        print("7. Demonstrate for loop usage")
        print("8. Demonstrate while loop usage")
        print("9. Exit")
        
        choice = input("\nEnter your choice (1-9): ")
        
        # Using if/else statements for menu navigation (fulfills conditional requirement)
        if choice == '1':
            word = input("Enter the word to search for: ")
            count = count_specific_word(article, word)
            print(f"\nThe word '{word}' appears {count} times in the article.")
            
        elif choice == '2':
            most_common = identify_most_common_word(article)
            print(f"\nThe most common word is: '{most_common}'")
            
        elif choice == '3':
            avg_length = calculate_average_word_length(article)
            print(f"\nAverage word length: {avg_length} characters")
            
        elif choice == '4':
            paragraphs = count_paragraphs(article)
            print(f"\nNumber of paragraphs: {paragraphs}")
            
        elif choice == '5':
            sentences = count_sentences(article)
            print(f"\nNumber of sentences: {sentences}")
            
        elif choice == '6':
            print("\n" + "="*50)
            print("COMPLETE ARTICLE ANALYSIS")
            print("="*50)
            print(f"Number of paragraphs: {count_paragraphs(article)}")
            print(f"Number of sentences: {count_sentences(article)}")
            print(f"Most common word: '{identify_most_common_word(article)}'")
            print(f"Average word length: {calculate_average_word_length(article)} characters")
            
            # Additional analysis specific to this article
            print("\nArticle-Specific Analysis:")
            print(f"Occurrences of 'Apple Pie Master': {count_specific_word(article, 'Apple Pie Master')}")
            print(f"Occurrences of 'ACME Inc.': {count_specific_word(article, 'ACME Inc.')}")
            print(f"Occurrences of 'AI': {count_specific_word(article, 'AI')}")
            
        elif choice == '7':
            demonstrate_for_loop_usage(article)
            
        elif choice == '8':
            demonstrate_while_loop_usage()
            
        elif choice == '9':
            print("\nExiting program. Thank you for using the News Article Analysis Tool!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")
        
        input("\nPress Enter to continue...")

# Run the main function when script is executed
if __name__ == "__main__":
    main()