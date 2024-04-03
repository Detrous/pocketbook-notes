import { publicGateway } from "../../config";

export interface RequestAllNotesResult {
  book_id: number;
  quote: string;
  context: string;
  language: string;
  translation: string;
  added_at: string;
}

export const requestAllNotes = async (query: string): Promise<RequestAllNotesResult[]> => {
  const response = await publicGateway(
    process.env.REACT_APP_API_HOST as string
  ).get(`/api/notes?query=${query}`);

  return response.data;
};
