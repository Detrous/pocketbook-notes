import { FC } from "react";
import { Box, Typography, Card, CardContent, Button } from "@mui/material";

import { BookItem } from "../../api/endpoints/requests/requestAllBooks";
import { Link } from "react-router-dom";

interface NoteCardProps {
  book: BookItem;
}

const BookCard: FC<NoteCardProps> = ({ book }) => {
  return (
    <Box sx={{ mb: 2, width: 1 / 2.2 }}>
      <Card variant="outlined">
        <CardContent>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            TBD
          </Typography>
          <Typography variant="h5" component="div">
            {book.title}
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            {book.authors}
          </Typography>
          <Typography variant="body2">Notes: {book.notes_count}</Typography>
        </CardContent>
        <Box>
          <Button
            key={"Words"}
            component={Link}
            to={`/words?book_id=${book.id}`}
          >
            View notes
          </Button>
        </Box>
      </Card>
    </Box>
  );
};

export default BookCard;
