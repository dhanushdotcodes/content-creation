export interface HealthResponse {
  success: boolean;
  data?: {
    status: string;
    database: string;
    timestamp: string;
  };
  error?: string;
}
