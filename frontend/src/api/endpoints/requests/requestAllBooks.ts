import { publicGateway } from "../../config";

export interface BookItem {
  id: number;
  title: string;
  authors: string;
  notes_count: number;
}

export const requestAllBooks = async (): Promise<BookItem[]> => {
  const response = await publicGateway(
    process.env.REACT_APP_API_HOST as string
  ).get(`/api/books`);

  return response.data;
};
