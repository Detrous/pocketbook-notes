import { publicGateway } from "../../config";

export interface BookItem {
  id: number;
  title: string;
  authors: string;
  notes_count: number;
}

export const requestBookInfo = async (book_id: string): Promise<BookItem> => {
  const response = await publicGateway(
    process.env.REACT_APP_API_HOST as string,
  ).get(`/api/books/${book_id}`);

  return response.data;
};
