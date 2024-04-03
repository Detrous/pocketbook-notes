import { useEffect, useState } from "react";
import { requestAllNotes, RequestAllNotesResult } from "../../api/endpoints";
import { Box, Input, Typography } from "@mui/material";
import NoteCard from "../../components/NoteCard/NoteCard";
import { useSearchParams } from "react-router-dom";
import { requestBookInfo } from "../../api/endpoints/requests/requestBookInfo";
import { BookItem } from "../../api/endpoints/requests/requestAllBooks";

const Words = () => {
  const [notes, setNotes] = useState<RequestAllNotesResult[]>([]);
  const [book, setBook] = useState<BookItem | null>(null);
  const [notesQuery, setNotesQuery] = useState('');
  const [searchParams] = useSearchParams();

  useEffect(() => {
    setBook(null);
    setNotes([]);

    const book_id = searchParams.get("book_id");

    const fetchAllNotes = async () => {
      try {
        const response = await requestAllNotes(notesQuery, book_id);
        setNotes(response);
      } catch (error) {
        console.error("Failed to fetch documents count:", error);
      }
    };

    const fetchBookInfo = async () => {
      try {
        const response = await requestBookInfo(book_id!);
        setBook(response);
      } catch (error) {
        console.error("Failed to fetch documents count:", error);
      }
    }

    fetchAllNotes();

    if (book_id != null) {
      fetchBookInfo();
    }
  }, [notesQuery, searchParams ]);

  const handleWordsSearch = (event: React.ChangeEvent<HTMLTextAreaElement | HTMLInputElement>) => {
    setNotesQuery(event.target.value);
  }

  return (
    <Box>
      {book && (
        <Box sx={{ display: "flex", justifyContent: "center", mt: 3 }}>
          <Typography sx={{ fontSize: 30 }}gutterBottom>{ book.title }</Typography>
        </Box>
      )}
      <Box
        sx={{
          flexDirection: "column",
          display: "flex",
          alignItems: "center",
          mt: 3,
        }}
      >
        <Box sx={{mb: 4}}>

      <Input placeholder="Search..." onChange={handleWordsSearch}/>
        </Box>
        {notes.map((note) => (
          <NoteCard key={note.id} note={note} />
        ))}
      </Box>
    </Box>
  );
};

export default Words;
