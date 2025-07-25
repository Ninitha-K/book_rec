from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

# Homepage
def home(request):
    return render(request, 'hai/home.html')

# Signup
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            auth_login(request, user)
            return redirect('genres')
        else:
            return render(request, 'hai/signup.html', {'error': 'Username already exists'})

    return render(request, 'hai/signup.html')

# Login
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(request, username=user.username, password=password)
            if auth_user is not None:
                auth_login(request, auth_user)
                return redirect('genres')
            else:
                return render(request, 'hai/login.html', {'error': 'Incorrect password'})
        else:
            return render(request, 'hai/login.html', {'error': 'No user found with that email'})

    return render(request, 'hai/login.html')

# Logout
def logout_view(request):
    auth_logout(request)
    return redirect('home')

# Genres Page
@login_required(login_url='/login/')
def genres(request):
    journals = [
        'Horror', 'Romance', 'Thriller', 'Comedy', 'Adventure',
        'Science Fiction', 'Fantasy', 'Mystery', 'Historical',
        'Drama', 'Poetry', 'Crime', 'Biography', 'Self-Help',
        'Philosophy', 'Psychology', 'Children', 'Young Adult',
        'Classic', 'Mythology', 'War', 'Spirituality', 'Dystopian',
        'Memoir', 'Art', 'Music', 'Cookbook', 'Travel', 'Humor'
    ]
    return render(request, 'hai/genres.html', {'genres': journals})

# Books for Selected Genre
@login_required(login_url='/login/')
def genre_books(request, genre_name):
    books = {
        "horror": [
        {"title": "It", "author": "Stephen King", "description": "A shape-shifting creature terrorizes a small town."},
        {"title": "The Haunting of Hill House", "author": "Shirley Jackson", "description": "A chilling tale of a haunted mansion."},
        {"title": "The Shining", "author": "Stephen King", "description": "A family is snowbound in a haunted hotel."},
        {"title": "Dracula", "author": "Bram Stoker", "description": "The original vampire novel that started it all."},
        {"title": "Frankenstein", "author": "Mary Shelley", "description": "A scientist creates a monster from corpses."},
        {"title": "Mexican Gothic", "author": "Silvia Moreno-Garcia", "description": "A gothic horror set in 1950s Mexico."},
        {"title": "Bird Box", "author": "Josh Malerman", "description": "A mysterious force drives people to madness if seen."}
    ],
        'romance': [
            {'title': 'The Notebook', 'author': 'Nicholas Sparks'},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
        ],
        'thriller': [
            {'title': 'Gone Girl', 'author': 'Gillian Flynn'},
            {'title': 'The Da Vinci Code', 'author': 'Dan Brown'},
        ],
        'comedy': [
            {'title': 'Good Omens', 'author': 'Neil Gaiman & Terry Pratchett'},
            {'title': 'Bossypants', 'author': 'Tina Fey'},
        ],
        'adventure': [
            {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'},
            {'title': 'Life of Pi', 'author': 'Yann Martel'},
        ],
        'science fiction': [
            {'title': 'Dune', 'author': 'Frank Herbert'},
            {'title': '1984', 'author': 'George Orwell'},
        ],
        'fantasy': [
            {'title': 'Harry Potter', 'author': 'J.K. Rowling'},
            {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
        ],
        'mystery': [
            {'title': 'Sherlock Holmes', 'author': 'Arthur Conan Doyle'},
            {'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson'},
        ],
        'historical': [
            {'title': 'The Book Thief', 'author': 'Markus Zusak'},
            {'title': 'The Help', 'author': 'Kathryn Stockett'},
        ],
        'drama': [
            {'title': 'Death of a Salesman', 'author': 'Arthur Miller', 'description': 'A tragic story of a man chasing the American dream.'},
            {'title': 'A Streetcar Named Desire', 'author': 'Tennessee Williams', 'description': 'A powerful drama about mental health and society.'},
            {'title': 'Long Day’s Journey Into Night', 'author': 'Eugene O’Neill', 'description': 'An intense family drama exploring addiction and regret.'},
            {'title': 'The Crucible', 'author': 'Arthur Miller', 'description': 'A dramatization of the Salem witch trials reflecting paranoia and injustice.'},
            {'title': 'Fences', 'author': 'August Wilson', 'description': 'A story about African American family life in the 1950s.'},
            {'title': 'The Glass Menagerie', 'author': 'Tennessee Williams', 'description': 'A memory play dealing with dreams and disappointment.'}
        ],
        'poetry': [
            {'title': 'The Sun and Her Flowers', 'author': 'Rupi Kaur', 'description': 'Poetry of love, loss, trauma, and healing.'},
            {'title': 'Milk and Honey', 'author': 'Rupi Kaur', 'description': 'Poems that speak to pain and strength.'},
            {'title': 'Leaves of Grass', 'author': 'Walt Whitman', 'description': 'Celebration of nature and the self.'},
            {'title': 'The Waste Land', 'author': 'T.S. Eliot', 'description': 'A modernist masterpiece of fragmentation and despair.'},
            {'title': 'Ariel', 'author': 'Sylvia Plath', 'description': 'Dark, emotional poems from a brilliant mind.'},
            {'title': 'Selected Poems', 'author': 'Emily Dickinson', 'description': 'Deep philosophical and romantic reflections.'}
        ],
        'crime': [
            {'title': 'In Cold Blood', 'author': 'Truman Capote'},
            {'title': 'The Snowman', 'author': 'Jo Nesbø'},
        ],
         'biography': [
            {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'description': 'A personal diary from the Holocaust era.'},
            {'title': 'Steve Jobs', 'author': 'Walter Isaacson', 'description': 'The life of the Apple co-founder and tech visionary.'},
            {'title': 'Long Walk to Freedom', 'author': 'Nelson Mandela', 'description': 'Autobiography of the iconic South African leader.'},
            {'title': 'Becoming', 'author': 'Michelle Obama', 'description': 'A memoir of the former First Lady of the United States.'},
            {'title': 'Einstein: His Life and Universe', 'author': 'Walter Isaacson', 'description': 'A deep dive into the mind of the genius physicist.'},
            {'title': 'The Story of My Experiments with Truth', 'author': 'Mahatma Gandhi', 'description': 'Autobiography of the leader of Indian independence.'}
        ],
        'self-help': [
            {'title': 'Atomic Habits', 'author': 'James Clear'},
            {'title': 'The Power of Now', 'author': 'Eckhart Tolle'},
        ],
        'philosophy': [
            {'title': 'Meditations', 'author': 'Marcus Aurelius'},
            {'title': 'The Republic', 'author': 'Plato'},
        ],
        'psychology': [
            {'title': 'Thinking, Fast and Slow', 'author': 'Daniel Kahneman'},
            {'title': 'The Power of Habit', 'author': 'Charles Duhigg'},
        ],
        'children': [
            {'title': 'Charlotte’s Web', 'author': 'E.B. White', 'description': 'A tender story about friendship between a pig and a spider.'},
            {'title': 'Matilda', 'author': 'Roald Dahl', 'description': 'A brilliant young girl uses her talents to fight back against tyranny.'},
            {'title': 'The Cat in the Hat', 'author': 'Dr. Seuss', 'description': 'A mischievous cat brings chaos and fun into children’s lives.'},
            {'title': 'The Gruffalo', 'author': 'Julia Donaldson', 'description': 'A clever mouse invents a monster to protect himself.'},
            {'title': 'Where the Wild Things Are', 'author': 'Maurice Sendak', 'description': 'A boy journeys to a land of wild creatures.'},
            {'title': 'The Tale of Peter Rabbit', 'author': 'Beatrix Potter', 'description': 'A curious rabbit gets into trouble in a vegetable garden.'}
        ],
        'young adult': [
            {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'description': 'A dystopian survival game turns into a rebellion.'},
            {'title': 'Divergent', 'author': 'Veronica Roth', 'description': 'A society divided by traits faces disruption.'},
            {'title': 'The Fault in Our Stars', 'author': 'John Green', 'description': 'Two teens with cancer fall in love.'},
            {'title': 'Looking for Alaska', 'author': 'John Green', 'description': 'A story about first love, loss, and growth.'},
            {'title': 'Thirteen Reasons Why', 'author': 'Jay Asher', 'description': 'A teen unravels a classmate’s reasons for suicide.'},
            {'title': 'Miss Peregrine’s Home for Peculiar Children', 'author': 'Ransom Riggs', 'description': 'Strange children with powers hide from danger.'}
        ],
        'classic': [
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
            {'title': 'Great Expectations', 'author': 'Charles Dickens'},
        ],
        'mythology': [
            {'title': 'Norse Mythology', 'author': 'Neil Gaiman'},
            {'title': 'Mythos', 'author': 'Stephen Fry'},
        ],
        'war': [
            {'title': 'Unbroken', 'author': 'Laura Hillenbrand'},
            {'title': 'All Quiet on the Western Front', 'author': 'Erich Maria Remarque'},
        ],
        'spirituality': [
            {'title': 'The Alchemist', 'author': 'Paulo Coelho'},
            {'title': 'Siddhartha', 'author': 'Hermann Hesse'},
        ],
        'dystopian': [
            {'title': 'The Handmaid’s Tale', 'author': 'Margaret Atwood'},
            {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury'},
        ],
        'memoir': [
            {'title': 'Educated', 'author': 'Tara Westover'},
            {'title': 'Born a Crime', 'author': 'Trevor Noah'},
        ],
        'art': [
            {'title': 'The Story of Art', 'author': 'E.H. Gombrich'},
            {'title': 'Ways of Seeing', 'author': 'John Berger'},
        ],
        'music': [
            {'title': 'Just Kids', 'author': 'Patti Smith'},
            {'title': 'Life', 'author': 'Keith Richards'},
        ],
        'cookbook': [
            {'title': 'Salt, Fat, Acid, Heat', 'author': 'Samin Nosrat'},
            {'title': 'The Joy of Cooking', 'author': 'Irma S. Rombauer'},
        ],
        'travel': [
            {'title': 'Into the Wild', 'author': 'Jon Krakauer'},
            {'title': 'Eat, Pray, Love', 'author': 'Elizabeth Gilbert'},
        ],
        'humor': [
            {'title': 'Yes Please', 'author': 'Amy Poehler'},
            {'title': 'Bossypants', 'author': 'Tina Fey'},
        ],
    }
    selected_books = books.get(genre_name.lower(), [])
    return render(request, 'hai/book_list.html', {
        'genre': genre_name.title(),
        'books': selected_books
    })
