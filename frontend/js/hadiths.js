async function loadHadiths() {

    const params = new URLSearchParams(window.location.search);

    const slug = params.get("book");

    if (!slug) {
        document.getElementById("book-title").textContent =
            "Kitab tidak ditemukan";

        document.getElementById("hadiths").textContent =
            "Parameter kitab tidak tersedia.";

        return;
    }

    // Ambil informasi kitab
    const bookResponse = await fetch(API_URL + "/books/" + slug);
    const book = await bookResponse.json();

    document.getElementById("book-title").textContent =
        book.title_en;

    // Ambil daftar hadis
    const hadithResponse = await fetch(
        API_URL + "/books/" + slug + "/hadiths"
    );

    const hadiths = await hadithResponse.json();

    const container = document.getElementById("hadiths");

    container.innerHTML = "";

    hadiths.forEach(hadith => {

        const div = document.createElement("div");

        div.className = "book";

        div.innerHTML = `
            <strong>Hadith ${hadith.hadith_number}</strong><br>
            ${hadith.translation_id.substring(0, 120)}...
        `;

        div.onclick = () => {

            window.location.href =
                `hadith.html?book=${slug}&number=${hadith.hadith_number}`;

        };

        container.appendChild(div);

    });

}

loadHadiths();