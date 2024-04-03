import { publicGateway } from "../../config";

export interface RequestAllNotesResult {
  id: number;
  book_id: number;
  book_name: string;
  quote: string;
  context: string;
  language: string;
  translation: string;
  added_at: string;
}

export const requestAllNotes = async (query: string, book_id: string | null): Promise<RequestAllNotesResult[]> => {
  var path = `/api/notes?query=${query}`;
  if (book_id != null) {
    path += `&book_id=${book_id}`;
  }

  const response = await publicGateway(
    process.env.REACT_APP_API_HOST as string
  ).get(path);

  return response.data;
};
