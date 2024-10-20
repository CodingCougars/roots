function goToProfile() {
    window.location.href = 'myProfile.html';
  }
  function goToArtifact() {
    window.location.href = 'addArtifact.html';
  }
  const posts = {
    /*food: [
      "Shami Kebab",
      "Aloo Tikki",
      "Seekh Kebab"
    ],
    art: [
      "Truck Art","Kalash Oil Painting", "Calligraphy"
    ],
    language: [
      "Excerpt of Text",
      "Multani Script", 
      "Mastering Mandarin", "Discovering German","Piece of Text"
    ]*/
  };
  
  function loadPosts() {
    for (const category in posts) {
      const scrollItems = document.querySelector(`#${category} .scroll-items`);
      const existingPosts = Array.from(scrollItems.children).map(post => post.textContent);
      posts[category].forEach(post => {
        const postDiv = document.createElement('div');
        postDiv.className = 'post';
        postDiv.textContent = post;
        scrollItems.appendChild(postDiv);
      });
    }
  }
  
  function createScrollToTopButton() {
    const button = document.createElement('button');
    button.textContent = 'Scroll to Top';
    button.id = 'scrollToTopBtn';
    button.style.display = 'none'; // Initially hidden
    button.onclick = () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    };
    document.body.appendChild(button);
  
    window.onscroll = () => {
      if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        button.style.display = 'block';
      } else {
        button.style.display = 'none';
      }
    };
  }
  
  function scrollRight(category) {
    const scrollContainer = document.querySelector(`#${category} .scroll-container`);
    scrollContainer.scrollBy({
      left: 220,
      behavior: 'smooth'
    });
  }
  
  window.onload = loadPosts;
  