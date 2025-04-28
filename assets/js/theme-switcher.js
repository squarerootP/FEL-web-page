document.addEventListener('DOMContentLoaded', function() {
  // Create link element for the theme CSS
  const themeLink = document.createElement('link');
  themeLink.rel = 'stylesheet';
  themeLink.href = './assets/css/black-gold-theme.css';
  
  // Add it to the head of the document
  document.head.appendChild(themeLink);
  
  console.log('Black-Gold theme applied successfully');
});
