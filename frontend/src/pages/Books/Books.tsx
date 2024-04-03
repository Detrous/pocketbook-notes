import { useEffect, useState } from "react";
import { BookItem, requestAllBooks } from "../../api/endpoints/requests/requestAllBooks";
import { Box, Input } from "@mui/material";
import BookCard from "../../components/BookCard";

const Books = () => {
  const [books, setBooks] = useState<BookItem[]>([]);

  useEffect(() => {
    const fetchAllBooks = async () => {
      try {
        const response = await requestAllBooks();
        setBooks(response);
      } catch (error) {
        console.error("Failed to fetch documents count:", error);
      }
    };

    fetchAllBooks();
  }, []);

  return (
      <Box>

      <Box
        sx={{
          flexDirection: "column",
          display: "flex",
          alignItems: "center",
          mt: 3,
        }}
      >
        <Box sx={{mb: 4}}>

      </Box>
        {books.map((book) => (
          <BookCard key={book.id} book={book} />
        ))}
      </Box>
    </Box>
  );
};

export default Books;
