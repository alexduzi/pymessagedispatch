CREATE PROCEDURE `GET_SERVICES` ()
BEGIN
	SELECT	services.ID,
			services.ServicesName,
            services.Host
    FROM 	ServicesQueue;
END
