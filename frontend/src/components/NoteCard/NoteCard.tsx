import { FC, useState } from "react";
import { RequestAllNotesResult } from "../../api/endpoints";
import {
  Box,
  Typography,
  Card,
  CardContent,
  CardActions,
  Button,
  Accordion, AccordionActions, AccordionSummary, AccordionDetails
} from "@mui/material";

import ExpandMoreIcon from '@mui/icons-material/ExpandMore';

interface NoteCardProps {
  note: RequestAllNotesResult;
}

const NoteCard: FC<NoteCardProps> = ({ note }) => {

    const [translationExpanded, setTranslationExpanded] = useState(false);

  const handleTranslationAccordion = () => (event: React.SyntheticEvent, isExpanded: boolean) => {
        setTranslationExpanded(isExpanded ? true : false);
    };



  return (
    <Box sx={{ mb: 2, width: 1 / 2.2 }}>
      <Card variant="outlined">
        <CardContent>
          <Typography sx={{ fontSize: 14 }} color="text.secondary" gutterBottom>
            { note.book_name }
          </Typography>
          <Typography variant="h5" component="div">
            {note.quote}
          </Typography>
          <Typography sx={{ mb: 1.5 }} color="text.secondary">
            TBD
          </Typography>
          <Typography variant="body2">{note.context}</Typography>
        </CardContent>
        <Accordion
          expanded={translationExpanded}
          onChange={handleTranslationAccordion()}
        >
          <AccordionSummary
            expandIcon={<ExpandMoreIcon />}
            aria-controls="panel1bh-content"
            id="panel1bh-header"
          >
            <Typography sx={{ width: "33%", flexShrink: 0 }}>
              Translation
            </Typography>
          </AccordionSummary>
          <AccordionDetails>
            <Typography>
              {note.translation ? note.translation.split('\n').map(str => <p>{str}</p>) : ''}
            </Typography>
          </AccordionDetails>
        </Accordion>
      </Card>
    </Box>
  );
};

export default NoteCard;
