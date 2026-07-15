async function loadBooks() {

    const response = await fetch(API_URL + "/books");

    const books = await response.json();

    const container = document.getElementById("books");

    container.innerHTML = "";

    books.forEach(book => {

        const div = document.createElement("div");

        div.className = "book";

        div.innerHTML = `
            <strong>${book.title_en}</strong><br>
            ${book.author_en}<br>
            ${book.total_hadith} Hadith
        `;

        div.onclick = () => {
            window.location.href =
                `hadiths.html?book=${book.slug}`;
        };

        container.appendChild(div);

    });

}

loadBooks();