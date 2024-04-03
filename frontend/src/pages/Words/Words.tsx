import { useEffect, useState } from "react";
import { requestAllNotes, RequestAllNotesResult } from "../../api/endpoints";
import { Box, Input } from "@mui/material";
import NoteCard from "../../components/NoteCard/NoteCard";

const Words = () => {
  const [notes, setNotes] = useState<RequestAllNotesResult[]>([]);
  const [query, setQuery] = useState('');

  useEffect(() => {
    const fetchAllNotes = async () => {
      try {
        const response = await requestAllNotes(query);
        setNotes(response);
      } catch (error) {
        console.error("Failed to fetch documents count:", error);
      }
    };

    fetchAllNotes();
  }, [query ]);

  const handleWordsSearch = (event: React.ChangeEvent<HTMLTextAreaElement | HTMLInputElement>) => {
    setQuery(event.target.value);
  }

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

      <Input placeholder="Search..." onChange={handleWordsSearch}/>
        </Box>
        {notes.map((note) => (
          <NoteCard note={note} />
        ))}
      </Box>
    </Box>
  );
};

export default Words;
