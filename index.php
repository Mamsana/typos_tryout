<html>
  <head>
      <title>Text Correction</title>
  </head>
  <body>
<?php
echo "sth"
      <h1>Correct Typos in Your Text</h1>
      <form action="/" method="post">
        <textarea name="text"></textarea>
        <br>
        <input type="submit" value="Submit">
      </form>
      {% if corrected_text %}
        <h2>Corrected Text:</h2>
        <p>{{ corrected_text }}</p>
      {% endif %}
      ?>
    </body>
</html>
