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
        'horror': [
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
    {'title': 'Me Before You', 'author': 'Jojo Moyes'},
    {'title': 'Outlander', 'author': 'Diana Gabaldon'},
    {'title': 'The Time Traveler’s Wife', 'author': 'Audrey Niffenegger'},
    {'title': 'Twilight', 'author': 'Stephenie Meyer'},
    {'title': 'The Fault in Our Stars', 'author': 'John Green'},
    {'title': 'Red, White & Royal Blue', 'author': 'Casey McQuiston'},
    {'title': 'The Hating Game', 'author': 'Sally Thorne'},
    {'title': 'Beach Read', 'author': 'Emily Henry'}
],
        'thriller': [
    {'title': 'Gone Girl', 'author': 'Gillian Flynn'},
    {'title': 'The Da Vinci Code', 'author': 'Dan Brown'},
    {'title': 'The Girl on the Train', 'author': 'Paula Hawkins'},
    {'title': 'The Silent Patient', 'author': 'Alex Michaelides'},
    {'title': 'Before I Go to Sleep', 'author': 'S.J. Watson'},
    {'title': 'Behind Closed Doors', 'author': 'B.A. Paris'},
    {'title': 'The Woman in the Window', 'author': 'A.J. Finn'},
    {'title': 'Sharp Objects', 'author': 'Gillian Flynn'},
    {'title': 'The Reversal', 'author': 'Michael Connelly'},
    {'title': 'I Am Watching You', 'author': 'Teresa Driscoll'}
],
        'comedy': [
    {'title': 'Good Omens', 'author': 'Neil Gaiman & Terry Pratchett'},
    {'title': 'Bossypants', 'author': 'Tina Fey'},
    {'title': 'Is Everyone Hanging Out Without Me?', 'author': 'Mindy Kaling'},
    {'title': 'Bridget Jones’s Diary', 'author': 'Helen Fielding'},
    {'title': 'Catch-22', 'author': 'Joseph Heller'},
    {'title': 'My Sister, the Serial Killer', 'author': 'Oyinkan Braithwaite'},
    {'title': 'Hyperbole and a Half', 'author': 'Allie Brosh'},
    {'title': 'Me Talk Pretty One Day', 'author': 'David Sedaris'},
    {'title': 'Dear Girls', 'author': 'Ali Wong'},
    {'title': 'Calypso', 'author': 'David Sedaris'}
     ],
        
        'science fiction': [
    {'title': 'Dune', 'author': 'Frank Herbert'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'Brave New World', 'author': 'Aldous Huxley'},
    {'title': 'Ender’s Game', 'author': 'Orson Scott Card'},
    {'title': 'Neuromancer', 'author': 'William Gibson'},
    {'title': 'Snow Crash', 'author': 'Neal Stephenson'},
    {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury'},
    {'title': 'The Left Hand of Darkness', 'author': 'Ursula K. Le Guin'},
    {'title': 'The Martian', 'author': 'Andy Weir'},
    {'title': 'Hyperion', 'author': 'Dan Simmons'}
    ],
     'science fiction': [
            {'title': 'Dune', 'author': 'Frank Herbert'},
            {'title': '1984', 'author': 'George Orwell'},
            {'title': 'Brave New World', 'author': 'Aldous Huxley'},
            {'title': 'Ender’s Game', 'author': 'Orson Scott Card'},
            {'title': 'Neuromancer', 'author': 'William Gibson'},
            {'title': 'Snow Crash', 'author': 'Neal Stephenson'},
            {'title': 'Fahrenheit 451', 'author': 'Ray Bradbury'},
            {'title': 'The Left Hand of Darkness', 'author': 'Ursula K. Le Guin'},
            {'title': 'The Martian', 'author': 'Andy Weir'},
            {'title': 'Hyperion', 'author': 'Dan Simmons'}
        ],
         'mystery': [
            {'title': 'Sherlock Holmes', 'author': 'Arthur Conan Doyle'},
            {'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson'},
        ],
        'historical': [
            {'title': 'The Book Thief', 'author': 'Markus Zusak'},
            {'title': 'All the Light We Cannot See', 'author': 'Anthony Doerr'},
            {'title': 'The Nightingale', 'author': 'Kristin Hannah'},
            {'title': 'The Pillars of the Earth', 'author': 'Ken Follett'},
            {'title': 'War and Peace', 'author': 'Leo Tolstoy'},
            {'title': 'Memoirs of a Geisha', 'author': 'Arthur Golden'},
            {'title': 'Wolf Hall', 'author': 'Hilary Mantel'},
            {'title': 'A Gentleman in Moscow', 'author': 'Amor Towles'},
            {'title': 'Homegoing', 'author': 'Yaa Gyasi'},
            {'title': 'Beloved', 'author': 'Toni Morrison'}
        ],
        'fantasy': [
    {'title': 'Harry Potter and the Sorcerer\'s Stone', 'author': 'J.K. Rowling'},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien'},
    {'title': 'A Game of Thrones', 'author': 'George R.R. Martin'},
    {'title': 'The Name of the Wind', 'author': 'Patrick Rothfuss'},
    {'title': 'Mistborn', 'author': 'Brandon Sanderson'},
    {'title': 'The Way of Kings', 'author': 'Brandon Sanderson'},
    {'title': 'The Wheel of Time', 'author': 'Robert Jordan'},
    {'title': 'Eragon', 'author': 'Christopher Paolini'},
    {'title': 'The Chronicles of Narnia', 'author': 'C.S. Lewis'},
    {'title': 'Shadow and Bone', 'author': 'Leigh Bardugo'}
],
     'adventure': [
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien'},
    {'title': 'Treasure Island', 'author': 'Robert Louis Stevenson'},
    {'title': 'Life of Pi', 'author': 'Yann Martel'},
    {'title': 'Into the Wild', 'author': 'Jon Krakauer'},
    {'title': 'The Call of the Wild', 'author': 'Jack London'},
    {'title': 'Journey to the Center of the Earth', 'author': 'Jules Verne'},
    {'title': 'The Lost World', 'author': 'Arthur Conan Doyle'},
    {'title': 'Hatchet', 'author': 'Gary Paulsen'},
    {'title': 'The Alchemist', 'author': 'Paulo Coelho'},
    {'title': 'The Maze Runner', 'author': 'James Dashner'}
],
"mystery": [
    {"title": "The Hound of the Baskervilles", "author": "Arthur Conan Doyle", "description": "Sherlock Holmes investigates a legendary beast haunting the moors."},
    {"title": "Gone Girl", "author": "Gillian Flynn", "description": "A wife goes missing, and secrets unravel in a suspenseful psychological thriller."},
    {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "description": "A journalist and hacker uncover dark secrets in a wealthy Swedish family."},
    {"title": "In the Woods", "author": "Tana French", "description": "A detective investigates a murder that may be tied to his own traumatic past."},
    {"title": "The Woman in White", "author": "Wilkie Collins", "description": "A classic Victorian mystery with secrets, mistaken identity, and suspense."},
    {"title": "The Secret History", "author": "Donna Tartt", "description": "A group of classics students hide a murder, leading to paranoia and guilt."},
    {"title": "The No. 1 Ladies’ Detective Agency", "author": "Alexander McCall Smith", "description": "Botswana's first female private detective solves quirky mysteries with heart."},
    {"title": "Big Little Lies", "author": "Liane Moriarty", "description": "Murder and secrets lie beneath the surface of suburban mom life."},
    {"title": "And Then There Were None", "author": "Agatha Christie", "description": "Ten strangers trapped on an island die one by one—can any survive?"},
    {"title": "The Cuckoo’s Calling", "author": "Robert Galbraith", "description": "A private detective investigates a supermodel’s suspicious death."}
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
        
         'biography': [
            {'title': 'The Diary of a Young Girl', 'author': 'Anne Frank', 'description': 'A personal diary from the Holocaust era.'},
            {'title': 'Steve Jobs', 'author': 'Walter Isaacson', 'description': 'The life of the Apple co-founder and tech visionary.'},
            {'title': 'Long Walk to Freedom', 'author': 'Nelson Mandela', 'description': 'Autobiography of the iconic South African leader.'},
            {'title': 'Becoming', 'author': 'Michelle Obama', 'description': 'A memoir of the former First Lady of the United States.'},
            {'title': 'Einstein: His Life and Universe', 'author': 'Walter Isaacson', 'description': 'A deep dive into the mind of the genius physicist.'},
            {'title': 'The Story of My Experiments with Truth', 'author': 'Mahatma Gandhi', 'description': 'Autobiography of the leader of Indian independence.'}
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

    'crime': [
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson"},
        {"title": "The Silence of the Lambs", "author": "Thomas Harris"},
        {"title": "In Cold Blood", "author": "Truman Capote"},
        {"title": "The Snowman", "author": "Jo Nesbø"},
        {"title": "I Am Watching You", "author": "Teresa Driscoll"}
    ],
    'self help': [
        {"title": "The Power of Now", "author": "Eckhart Tolle"},
        {"title": "Atomic Habits", "author": "James Clear"},
        {"title": "The 7 Habits of Highly Effective People", "author": "Stephen Covey"},
        {"title": "Think and Grow Rich", "author": "Napoleon Hill"},
        {"title": "The Subtle Art of Not Giving a F*ck", "author": "Mark Manson"}
    ],
    'philosophy': [
        {"title": "Meditations", "author": "Marcus Aurelius"},
        {"title": "The Republic", "author": "Plato"},
        {"title": "Thus Spoke Zarathustra", "author": "Friedrich Nietzsche"},
        {"title": "Being and Time", "author": "Martin Heidegger"},
        {"title": "Critique of Pure Reason", "author": "Immanuel Kant"}
    ],
    'psychology': [
        {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman"},
        {"title": "Man’s Search for Meaning", "author": "Viktor E. Frankl"},
        {"title": "The Interpretation of Dreams", "author": "Sigmund Freud"},
        {"title": "Flow", "author": "Mihaly Csikszentmihalyi"},
        {"title": "Behave", "author": "Robert Sapolsky"}
    ],
    'classic': [
        {"title": "Pride and Prejudice", "author": "Jane Austen"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "Moby-Dick", "author": "Herman Melville"},
        {"title": "Jane Eyre", "author": "Charlotte Brontë"}
    ],
    'mythology': [
        {"title": "Mythos", "author": "Stephen Fry"},
        {"title": "The Iliad", "author": "Homer"},
        {"title": "Ramayana", "author": "Valmiki"},
        {"title": "The Norse Myths", "author": "Kevin Crossley-Holland"},
        {"title": "The Mahabharata", "author": "Vyasa"}
    ],
    'wars': [
        {"title": "All Quiet on the Western Front", "author": "Erich Maria Remarque"},
        {"title": "The Things They Carried", "author": "Tim O'Brien"},
        {"title": "War and Peace", "author": "Leo Tolstoy"},
        {"title": "The Book Thief", "author": "Markus Zusak"},
        {"title": "With the Old Breed", "author": "E.B. Sledge"}
    ],
    'spirituality': [
        {"title": "The Bhagavad Gita", "author": "Vyasa"},
        {"title": "The Tao of Pooh", "author": "Benjamin Hoff"},
        {"title": "A New Earth", "author": "Eckhart Tolle"},
        {"title": "The Alchemist", "author": "Paulo Coelho"},
        {"title": "Autobiography of a Yogi", "author": "Paramahansa Yogananda"}
    ],
    'dystopian': [
        {"title": "1984", "author": "George Orwell"},
        {"title": "Brave New World", "author": "Aldous Huxley"},
        {"title": "Fahrenheit 451", "author": "Ray Bradbury"},
        {"title": "The Hunger Games", "author": "Suzanne Collins"},
        {"title": "The Handmaid’s Tale", "author": "Margaret Atwood"}
    ],
    'memoir': [
        {"title": "Educated", "author": "Tara Westover"},
        {"title": "Becoming", "author": "Michelle Obama"},
        {"title": "When Breath Becomes Air", "author": "Paul Kalanithi"},
        {"title": "Born a Crime", "author": "Trevor Noah"},
        {"title": "The Diary of a Young Girl", "author": "Anne Frank"}
    ],
    'art': [
        {"title": "The Story of Art", "author": "E.H. Gombrich"},
        {"title": "Ways of Seeing", "author": "John Berger"},
        {"title": "Steal Like an Artist", "author": "Austin Kleon"},
        {"title": "Art & Fear", "author": "David Bayles and Ted Orland"},
        {"title": "What Are You Looking At?", "author": "Will Gompertz"}
    ],
    'music': [
        {"title": "Just Kids", "author": "Patti Smith"},
        {"title": "Life", "author": "Keith Richards"},
        {"title": "Musicophilia", "author": "Oliver Sacks"},
        {"title": "This Is Your Brain on Music", "author": "Daniel Levitin"},
        {"title": "The Rest Is Noise", "author": "Alex Ross"}
    ],
    'cookbook': [
        {"title": "Salt, Fat, Acid, Heat", "author": "Samin Nosrat"},
        {"title": "The Joy of Cooking", "author": "Irma S. Rombauer"},
        {"title": "Mastering the Art of French Cooking", "author": "Julia Child"},
        {"title": "Plenty", "author": "Yotam Ottolenghi"},
        {"title": "Indian-ish", "author": "Priya Krishna"}
    ],
    'travel': [
        {"title": "Into the Wild", "author": "Jon Krakauer"},
        {"title": "Eat, Pray, Love", "author": "Elizabeth Gilbert"},
        {"title": "The Geography of Bliss", "author": "Eric Weiner"},
        {"title": "On the Road", "author": "Jack Kerouac"},
        {"title": "The Art of Travel", "author": "Alain de Botton"}
    ],
    'humor': [
        {"title": "Bossypants", "author": "Tina Fey"},
        {"title": "Good Omens", "author": "Neil Gaiman & Terry Pratchett"},
        {"title": "Is Everyone Hanging Out Without Me?", "author": "Mindy Kaling"},
        {"title": "Yes Please", "author": "Amy Poehler"},
        {"title": "Me Talk Pretty One Day", "author": "David Sedaris"}
    ]}   
    
    selected_books = books.get(genre_name.lower(), [])
    return render(request, 'hai/book_list.html', {
        'genre': genre_name.title(),
        'books': selected_books
    })
